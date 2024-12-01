import time;
from random import randint;
paragraphs = [
    "Learning to code can be a challenging but rewarding experience. With the right resources and dedication, anyone can become proficient in programming. It’s all about breaking down problems and solving them step by step.",
    
    "The internet has revolutionized how we communicate, work, and learn. From social media to online education, the web has opened up a world of possibilities. But with these advancements come new challenges, such as privacy and security concerns.",
    
    "A healthy mind is as important as a healthy body. Regular physical activity, good nutrition, and enough rest are essential to maintaining mental well-being. The mind and body are closely connected, and one cannot thrive without the other.",
    
    "Technology is advancing at an unprecedented rate, and it is shaping the future in ways we never imagined. Artificial intelligence, robotics, and blockchain are just a few of the innovations that are changing industries and societies globally.",
    
    "Books have the power to transport readers to different worlds, spark their imaginations, and broaden their perspectives. Whether it's fiction or non-fiction, reading is a gateway to gaining new knowledge and experiencing diverse cultures.",
    
    "The environment is facing many challenges, from pollution to climate change. It’s important for individuals, communities, and governments to work together to protect our planet and ensure a sustainable future for generations to come.",
    
    "Traveling is one of the most enriching experiences. It allows people to explore new places, meet diverse cultures, and learn about the world in ways that books or documentaries can't replicate. Every journey is a story in itself.",
    
    "Innovation often comes from a place of necessity. When people face problems that seem unsolvable, their creativity drives them to come up with new solutions. The most groundbreaking ideas are often born out of the need for change.",
    
    "The mind is a powerful tool. It can shape our experiences, influence our actions, and determine our future. With mindfulness and focus, we can harness the full potential of our thoughts and use them to create the life we desire.",
    
    "Social connections are vital for well-being. Strong relationships with family, friends, and colleagues can provide support, foster happiness, and reduce stress. It’s important to nurture these connections and be there for each other."
]

def cal_time(st,end):
    t=end-st
    return t/60

def cal_accuracy(org,s):
    c=0
    for a,b in zip(org,s):
        if(a==b):
            c=c+1
    
    return (c/len(org))*100

def main():
    print("Test your typing speed")
    i = randint(0, len(paragraphs)-1)
    original=paragraphs[i]
    print(original)
    print("*"*20)
    print("Start typing the line above")
    start_time=time.time()
    s=input()
    end_time=time.time()
    print("You took ",cal_time(start_time,end_time)," minutes to type")
    print("Accuracy", cal_accuracy(original,s))

if __name__=="__main__":
    main()

