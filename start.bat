@echo off
cd /d "%~dp0"
echo ========================================
echo   英検リーディング練習アプリ
echo   http://localhost:8085
echo ========================================
echo.
echo ブラウザで http://localhost:8085 を開いてください
echo 終了するには Ctrl+C を押してください
echo.
start http://localhost:8085
npx -y http-server . -p 8085 -c-1
pause
