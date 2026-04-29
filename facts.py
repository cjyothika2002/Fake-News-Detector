# facts.py
import re

def rule_based_check(text: str) -> bool:
    print(">>> RULE CHECK RUNNING <<<")

    t = text.lower()
    t = re.sub(r"\s+", " ", t)  # normalize spaces

    suspicious_patterns = [

        # 🌐 Internet shutdown hoaxes
        r"internet.*shut.*every sunday",
        r"internet.*suspend.*every sunday",
        r"internet.*ban.*every sunday",
        r"internet.*shutdown",
        r"social media.*ban.*tomorrow",

        # 🇮🇳 Permanently + nationwide
        r"permanently.*across india",
        r"permanently.*entire country",

        # 🏦 Bank / RBI hoaxes
        r"all banks.*closed",
        r"banks.*permanently closed",
        r"rbi.*close.*banks",
        r"banks.*refund.*everyone",

        # 📚 Exam hoaxes
        r"board exams.*cancelled",
        r"exams.*cancelled.*years",
        r"exam results.*leaked",
        r"results.*today.*guaranteed",

        # 💰 Government money hoaxes
        r"government.*give.*money",
        r"government.*deposit.*money",
        r"free.*money.*government",
        r"rs\s*\d+.*free",
        r"giveaway.*government.*money",

        # 🌕 Space / sky hoaxes
        r"moon.*turn.*color",
        r"sun.*turn.*color",
        r"sky.*turn.*color",
        r"planet.*close.*earth",
        r"earth.*end.*next week",

        # 🌪 Disaster hoaxes
        r"tsunami.*tomorrow",
        r"hurricane.*hit.*city.*tomorrow",
        r"earthquake.*predicted.*magnitude",
        r"volcano.*eruption.*next week",

        # 🧪 Health cure hoaxes
        r"drink.*hot water.*cure",
        r"cure.*diabetes.*days",
        r"eat.*herbs.*cancer.*cure",
        r"salt water.*cure",
        r"vaccines.*dangerous.*secret",

        # 📡 Technology panic hoaxes
        r"5g.*cause.*disease",
        r"wifi.*dangerous",
        r"mobile towers.*affect.*thoughts",

        # 🗳 Voting / election hoaxes
        r"vote.*via.*whatsapp",
        r"elections.*cancelled.*nationwide",
        r"voting.*online.*government",

        # 🎓 Scholarship / education hoaxes
        r"scholarship.*money.*everyone",
        r"fees.*waived.*college.*all students",
        r"university.*free.*degree",

        # 👥 Census / citizen hoaxes
        r"population.*double.*overnight",
        r"all citizens.*re-register",
    ]

    for pattern in suspicious_patterns:
        if re.search(pattern, t):
            print(">>> RULE MATCHED:", pattern)
            return True

    return False