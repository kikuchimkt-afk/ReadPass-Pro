import json
import os

data = {
    "id": "2026-1-sat",
    "name": "2026年度 第1回（土曜準会場）",
    "passages": [
        {
            "id": "1",
            "type": "vocabulary",
            "instruction": "次の英文の( )に入れるのに最も適切なものを1,2,3,4の中から一つ選びなさい。",
            "questions": [
                {
                    "id": "1",
                    "number": "1",
                    "text": "The teacher told the students to (        ) their essays before they handed them in. They had made many mistakes.",
                    "options": ["separate", "revise", "decrease", "greet"],
                    "answer": "2"
                },
                {
                    "id": "2",
                    "number": "2",
                    "text": "When the teacher told the students that they had done a good job on their homework, she made sure to (        ) the students who had worked especially hard.",
                    "options": ["struggle", "acknowledge", "squeeze", "publish"],
                    "answer": "2"
                },
                {
                    "id": "3",
                    "number": "3",
                    "text": "The charity concert raised a lot of money to (        ) the people affected by the earthquake. The concert organizers used the money to buy food and other supplies.",
                    "options": ["lie", "reward", "honor", "aid"],
                    "answer": "4"
                },
                {
                    "id": "4",
                    "number": "4",
                    "text": "There is no (        ) between the computers in the office. They all have the same software and hardware.",
                    "options": ["ratio", "challenge", "bargain", "distinction"],
                    "answer": "4"
                },
                {
                    "id": "5",
                    "number": "5",
                    "text": "A : Who is your favorite (        ), Maya?\nB : I really like the books by Kellan Storme. He wrote many interesting stories.",
                    "options": ["officer", "actor", "author", "engineer"],
                    "answer": "3"
                },
                {
                    "id": "6",
                    "number": "6",
                    "text": "A : I finished writing my report, but I don't have any pictures to go with it.\nB : You can (        ) some pictures from the Internet. Just make sure to write where you found them.",
                    "options": ["insert", "melt", "wander", "fold"],
                    "answer": "1"
                },
                {
                    "id": "7",
                    "number": "7",
                    "text": "The (        ) of students in the class thought that the history test was too difficult. Only a few students thought that it was easy.",
                    "options": ["manner", "majority", "relation", "potential"],
                    "answer": "2"
                },
                {
                    "id": "8",
                    "number": "8",
                    "text": "A : You look really tired. Are you OK?\nB : Well, I couldn't sleep well because I had a horrible (        ) about getting lost in a dark forest.",
                    "options": ["citizen", "nightmare", "display", "location"],
                    "answer": "2"
                },
                {
                    "id": "9",
                    "number": "9",
                    "text": "A : Congratulations on your promotion! You must feel proud.\nB : Thank you, but I'm just doing my job. I try to stay (        ) and focused on my work.",
                    "options": ["empty", "sore", "cruel", "humble"],
                    "answer": "4"
                },
                {
                    "id": "10",
                    "number": "10",
                    "text": "A : What are the ingredients in the pumpkin pie you made?\nB : Pumpkin, of course, and spices that are (        ) used in pumpkin pie, like cinnamon and nutmeg.",
                    "options": ["kindly", "legally", "commonly", "professionally"],
                    "answer": "3"
                },
                {
                    "id": "11",
                    "number": "11",
                    "text": "A : I think I'll go to the mall tomorrow.\nB : If you (        ) the bookstore, could you get me a copy of this month's fashion magazine?",
                    "options": ["give up", "figure out", "fall over", "drop by"],
                    "answer": "4"
                },
                {
                    "id": "12",
                    "number": "12",
                    "text": "A : Could you check the stationery cupboard? We might (        ) some supplies.\nB : You're right. We need to order more pens and folders.",
                    "options": ["be sure of", "be short of", "be free of", "be kind of"],
                    "answer": "2"
                },
                {
                    "id": "13",
                    "number": "13",
                    "text": "A : I think we should take the squirrel back to its nest.\nB : No, (        ). Its mother will come back for it.",
                    "options": ["move it on", "leave it alone", "throw it away", "take it over"],
                    "answer": "2"
                },
                {
                    "id": "14",
                    "number": "14",
                    "text": "A : Thank you for coming to the airport to (        ) my cousin.\nB : No problem. It's nice to have a chance to say goodbye in person.",
                    "options": ["show off", "hand out", "bring in", "see off"],
                    "answer": "4"
                },
                {
                    "id": "15",
                    "number": "15",
                    "text": "Harvey's family moved to a new town last month. (        ), he made some new friends at school, and he started to enjoy living there.",
                    "options": ["For free", "In demand", "On average", "Before long"],
                    "answer": "4"
                },
                {
                    "id": "16",
                    "number": "16",
                    "text": "When Sarah was young, she lived next to a bakery. Now, the smell of fresh bread always (        ) her childhood.",
                    "options": ["learns her from", "hears her from", "reminds her of", "talks her into"],
                    "answer": "3"
                },
                {
                    "id": "17",
                    "number": "17",
                    "text": "The weather forecast said it was going to rain all day, but it (        ) to be sunny. In fact, it was the hottest day of the year.",
                    "options": ["ran out", "put out", "turned out", "gave out"],
                    "answer": "3"
                }
            ]
        },
        {
            "id": "2A",
            "type": "reading",
            "instruction": "次の英文A, Bを読み、その文意にそって(18)から(23)までの( )に入れるのに最も適切なものを1,2,3,4の中から一つ選びなさい。",
            "content": {
                "title": "A Christmas Tradition",
                "body": "Every December, fans of a Spanish professional soccer team take part in a special event. On a certain day, they come to the stadium not only to watch a match but also to throw soft toys onto the field. Tens of thousands of such toys are thrown, and then they are immediately collected by volunteers. ( 18 ), these toys are delivered to children who are in need. This event is held every year, and it is a way for soccer fans to help bring joy to many children at this special time of the year.\nThis tradition began in 2018 ( 19 ). At that time, the soccer club and its fans wanted to do a kind act for local children who were less fortunate than others. Since then, the event has grown and turned into an occasion that even fans of other teams look forward to every year. Many people have been touched by the kind gesture of the club and its fans in organizing such an event, and call it a wonderful tradition.\nToday, it has grown into a larger tradition that ( 20 ). The toys are not only given to children in the local city. Some of the toys are sent to charity organizations in other parts of Spain and even to children overseas. By doing so, many children both inside and outside the country can receive presents during the Christmas season. Thanks to this event, more children can feel happy and celebrate this special time of the year."
            },
            "questions": [
                {
                    "id": "18",
                    "number": "18",
                    "text": "( 18 )",
                    "options": ["In contrast", "Eventually", "On the other hand", "Despite the fact"],
                    "answer": "2"
                },
                {
                    "id": "19",
                    "number": "19",
                    "text": "( 19 )",
                    "options": ["with a specific purpose in mind", "as part of a marketing campaign", "to compete with other clubs' events", "to celebrate the team's victory"],
                    "answer": "1"
                },
                {
                    "id": "20",
                    "number": "20",
                    "text": "( 20 )",
                    "options": ["focuses on entertaining the fans", "replaces Christmas gifts with tickets", "encourages the fans to bring food instead", "spreads kindness across nations"],
                    "answer": "4"
                }
            ]
        },
        {
            "id": "2B",
            "type": "reading",
            "instruction": "次の英文A, Bを読み、その文意にそって(18)から(23)までの( )に入れるのに最も適切なものを1,2,3,4の中から一つ選びなさい。",
            "content": {
                "title": "Traveling for Dental Care",
                "body": "These days, people travel abroad not only for fun or sightseeing but also for other purposes. One growing purpose is to receive dental care. This means that people visit other countries to get their teeth treated. This practice is known as dental tourism. In recent years, this trend has become common in many parts of the world. ( 21 ), data shows that people from countries such as Australia and the United Kingdom are traveling long distances for dental health.\nThere are several reasons for this trend. One reason is the high cost of treatment. Some types of dental care in Australia cost more than twice as much as in Thailand. Another reason is ( 22 ) in some countries. In a 2024 survey of more than 2,000 people in the United Kingdom, around 20 percent reported that they had tried to book a clinic visit in the past year but could not see a dentist. These factors lead people to receive dental care in other countries.\nAccording to experts, however, people should be careful about the dangers of dental tourism, because there is a possibility of receiving unnecessary treatment or getting treatment using low-quality materials. Also, they may not receive enough legal support if something goes wrong. Therefore, it is important to ( 23 ). By doing so, people can clearly understand the possible problems and make safe choices about getting dental care abroad. The trend of dental tourism also highlights the importance of providing easy access to dental care in all countries."
            },
            "questions": [
                {
                    "id": "21",
                    "number": "21",
                    "text": "( 21 )",
                    "options": ["By contrast", "As a result", "For example", "In the end"],
                    "answer": "3"
                },
                {
                    "id": "22",
                    "number": "22",
                    "text": "( 22 )",
                    "options": ["the long travel times between cities", "the difficulty of making appointments", "the lack of professional skills among dentists", "the poor quality of the machines used"],
                    "answer": "2"
                },
                {
                    "id": "23",
                    "number": "23",
                    "text": "( 23 )",
                    "options": ["collect information about the risks", "choose a clinic with good reviews", "avoid traveling for major dental work", "let the dentists make all the decisions"],
                    "answer": "1"
                }
            ]
        },
        {
            "id": "3A",
            "type": "reading",
            "instruction": "次の英文A, Bの内容に関して、(24)から(31)までの質問に対して最も適切なもの、または文を完成させるのに最も適切なものを1,2,3,4の中から一つ選びなさい。",
            "content": {
                "title": "Email",
                "body": "From: Emma Lawrence <contact@el-service.net>\nTo: Cooper Jenkins <cooper.w.jenkins@connet-globally.com>\nDate: June 20\nSubject: Service information\nDear Cooper,\nMy name is Emma Lawrence. Thank you for your email. I understand you are looking for someone to look after your dog while on a family trip during the school holidays. I am happy to tell you I am available on the dates you mentioned. I used to work as an animal doctor and have five years of experience as a dog sitter. I am confident that your dog will feel safe and comfortable with me.\nMy services usually include feeding dogs the food you provide, giving them water, and offering snacks if necessary. I take dogs for walks twice a day, for about an hour, and spend time playing with them. I also provide a comfortable place to sleep. However, I cannot prepare dog food, so I ask dog owners to bring their food. Please let me know if there is anything I should know about your dog, such as any health problems.\nThe daily fee is $50. I will be looking after your dog for three days, so the total will be $150. Payment is required before the service. Since you are under eighteen, please speak with your parents about my services, including the fee. Please respond by June 22 if you wish to use my services. I look forward to hearing from you.\nThank you,\nEmma Lawrence"
            },
            "questions": [
                {
                    "id": "24",
                    "number": "24",
                    "text": "Why did Cooper Jenkins contact Emma Lawrence at first?",
                    "options": ["To receive advice from an animal doctor.", "To know how to become a good dog sitter.", "To ask if he can take his dog on his trip.", "To request her service to care for his dog."],
                    "answer": "4"
                },
                {
                    "id": "25",
                    "number": "25",
                    "text": "In the email, Emma tells Cooper that",
                    "options": ["she wants to understand his dog's sleeping habits.", "she needs to know how often she should walk his dog.", "she cannot provide food for his dog on her own.", "she cannot welcome his dog if it has health problems."],
                    "answer": "3"
                },
                {
                    "id": "26",
                    "number": "26",
                    "text": "What does Emma ask Cooper to do?",
                    "options": ["Talk to his parents about the services and cost.", "Pay the service fee to her by June 22.", "Send her $50 in advance of the service.", "Reply to her in a week for an appointment."],
                    "answer": "1"
                }
            ]
        },
        {
            "id": "3B",
            "type": "reading",
            "instruction": "次の英文A, Bの内容に関して、(24)から(31)までの質問に対して最も適切なもの、または文を完成させるのに最も適切なものを1,2,3,4の中から一つ選びなさい。",
            "content": {
                "title": "Avocado Production",
                "body": "Today, many people are more concerned about their health than before. Therefore, foods that are considered healthy are gaining attention. Avocados have been a popular food in many countries around the world. Their health value is especially attractive to people whose diets are based on plants. For example, they contain high amounts of healthy fats, which are better than other kinds of fats found in meat. According to researchers, they can also help reduce the risk of heart disease.\nEspecially in many European countries and the United States, the number of people eating avocados has increased. Because these countries import a lot of avocados, they are responsible for a large part of the global avocado market. In Europe, countries like France and the United Kingdom have already experienced high demand. However, there is still room for the avocado market to grow in Italy and Eastern European countries, where the market is smaller. In other words, the avocado market in Europe could continue to grow.\nHowever, there are several problems with avocado production due to its increasing demand. For example, because the production requires a lot of water, increased demand puts pressure on water resources. This has created water shortage problems in production areas. Also, the mass production of avocados sometimes causes too much supply, which can lead to reduced prices for avocados. This means that avocado farmers may earn less money and find it harder to continue their business.\nTo help solve these problems, consumers can choose to buy avocados with the FAIRTRADE Mark. This system was introduced to the avocado industry in 2010. The mark means the avocados are produced in an eco-friendly way and that the farmers receive a fair amount of money. Also, these farmers receive extra money that can be used for their businesses or community projects to protect the environment. In this way, the avocado industry is working to create better working conditions and promote responsible farming for the future."
            },
            "questions": [
                {
                    "id": "27",
                    "number": "27",
                    "text": "One reason that avocados are gaining attention is that",
                    "options": ["eating too many of them can increase the risk of heart disease.", "they provide fats that are considered healthier than fats in meat.", "more people are choosing to be vegetarians to lose weight.", "there is zero fat to be found in them, unlike meat."],
                    "answer": "2"
                },
                {
                    "id": "28",
                    "number": "28",
                    "text": "What is the situation surrounding avocados in Europe?",
                    "options": ["Some countries, like the United Kingdom, have stopped importing avocados.", "Many European countries rely on the United States to import avocados.", "The custom of eating avocados will probably spread to France in the future.", "Italy and Eastern European countries will be key to expanding the avocado market in Europe."],
                    "answer": "4"
                },
                {
                    "id": "29",
                    "number": "29",
                    "text": "What is one of the problems with avocado production?",
                    "options": ["Avocado producers limit their supply to maintain a high price.", "Increased demand for avocados has caused labor shortages.", "Many avocado farmers produce avocados in a way that is against the law.", "Avocado prices fall if the supply is too high, reducing farmers' income."],
                    "answer": "4"
                },
                {
                    "id": "30",
                    "number": "30",
                    "text": "What is true about the system using the FAIRTRADE Mark in the avocado industry?",
                    "options": ["It ensures all avocados are sold only in local, eco-friendly markets.", "It provides the community with money if farmers use modern farming tools.", "It focuses mainly on reducing avocado prices in the international market.", "It allows farmers to earn fair pay and spend it on environmental protection."],
                    "answer": "4"
                },
                {
                    "id": "31",
                    "number": "31",
                    "text": "What do we learn from the passage?",
                    "options": ["The production of avocados helps solve water shortage problems.", "The United States is a major consumer in the avocado market.", "Avocados are especially popular among people who love meat.", "The FAIRTRADE Mark is no longer working out for avocado farmers."],
                    "answer": "2"
                }
            ]
        }
    ]
}

os.makedirs("data/grade-pre2plus/2026-1-sat", exist_ok=True)
with open("data/grade-pre2plus/2026-1-sat/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Created data.json successfully.")
