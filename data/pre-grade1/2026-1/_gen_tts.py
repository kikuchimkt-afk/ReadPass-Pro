# -*- coding: utf-8 -*-
"""Generate the 85 learning-audio files used by ReadPass Pre-1 2026-1."""

import asyncio
import hashlib
import json
import os
import re
import sys

import edge_tts


sys.stdout.reconfigure(encoding="utf-8")

VOICE = "en-US-JennyNeural"
RATE = "-15%"
BASE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE, "data.json")
AUDIO_DIR = os.path.join(BASE, "audio")
VOCAB_DIR = os.path.join(AUDIO_DIR, "vocab")
MANIFEST_PATH = os.path.join(AUDIO_DIR, "tts_manifest.json")


async def save_speech(text, path):
    temporary_path = f"{path}.tmp"
    try:
        speech = edge_tts.Communicate(text, VOICE, rate=RATE)
        await speech.save(temporary_path)
        if os.path.getsize(temporary_path) < 500:
            raise RuntimeError(f"generated audio is unexpectedly small: {path}")
        os.replace(temporary_path, path)
    finally:
        if os.path.exists(temporary_path):
            os.remove(temporary_path)


def signature(text):
    payload = json.dumps(
        {"rate": RATE, "text": text, "voice": VOICE},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def file_sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def needs_audio(path, relative_path, expected_signature, old_manifest):
    if not os.path.exists(path) or os.path.getsize(path) < 500:
        return True
    manifest_entry = old_manifest.get(relative_path)
    if isinstance(manifest_entry, str):
        return manifest_entry != expected_signature
    if not isinstance(manifest_entry, dict):
        return True
    return (
        manifest_entry.get("inputSha256") != expected_signature
        or manifest_entry.get("audioSha256") != file_sha256(path)
    )


if not os.path.exists(DATA_PATH):
    raise SystemExit("data.json is missing; run the Pre-1 generators first")

os.makedirs(VOCAB_DIR, exist_ok=True)
with open(DATA_PATH, encoding="utf-8") as handle:
    data = json.load(handle)
try:
    with open(MANIFEST_PATH, encoding="utf-8") as handle:
        old_manifest = json.load(handle)
    if not isinstance(old_manifest, dict):
        old_manifest = {}
except (FileNotFoundError, json.JSONDecodeError):
    old_manifest = {}

created = 0
expected_manifest = {}
focus_points = data.get("lessonPlan", {}).get("focusPoints", [])
for index, focus_point in enumerate(focus_points, 1):
    passage = focus_point.get("practicePassage", {})
    english = re.sub(r"\[出典:.*?\]\s*", "", passage.get("en", ""), count=1).strip()
    filename = f"practice_pp{index}.mp3"
    relative_path = f"audio/{filename}"
    output_path = os.path.join(AUDIO_DIR, filename)
    expected_signature = signature(english)
    if needs_audio(output_path, relative_path, expected_signature, old_manifest):
        print(f"Generating {relative_path} ...", flush=True)
        asyncio.run(save_speech(english, output_path))
        created += 1
    expected_manifest[relative_path] = {
        "audioSha256": file_sha256(output_path),
        "inputSha256": expected_signature,
    }
    passage["audioFile"] = relative_path

for index, item in enumerate(data.get("vocabulary", []), 1):
    slug = re.sub(r"[^a-zA-Z0-9_]", "_", item["word"].lower()).strip("_")
    filename = f"w_{index:03d}_{slug}.mp3"
    relative_path = f"audio/vocab/{filename}"
    output_path = os.path.join(VOCAB_DIR, filename)
    expected_signature = signature(item["word"])
    if needs_audio(output_path, relative_path, expected_signature, old_manifest):
        print(f"Generating {relative_path} ...", flush=True)
        asyncio.run(save_speech(item["word"], output_path))
        created += 1
    expected_manifest[relative_path] = {
        "audioSha256": file_sha256(output_path),
        "inputSha256": expected_signature,
    }
    item["wordAudio"] = relative_path

with open(DATA_PATH, "w", encoding="utf-8") as handle:
    json.dump(data, handle, ensure_ascii=False, indent=4)
    handle.write("\n")

manifest_temporary_path = f"{MANIFEST_PATH}.tmp"
with open(manifest_temporary_path, "w", encoding="utf-8") as handle:
    json.dump(expected_manifest, handle, ensure_ascii=False, indent=4, sort_keys=True)
    handle.write("\n")
os.replace(manifest_temporary_path, MANIFEST_PATH)

print(
    f"Done: {created} new / "
    f"{len(data.get('vocabulary', [])) + len(focus_points)} expected audio files"
)
