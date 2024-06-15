config['functions'] = [
    {"name": "finance",
     "description": "Is a large language model fine-tuned on earnings call documents to extract financial KPIs from the earnings call documents.",
     "condition": "Use this adapter when users asked you about finances or they need to analyze financial data.",
     # "keywords": ["finance", "financial data", "earnings", "reports", "KPIs", "investment", "stocks", "options"]
     },
    {"name": "medicine",
     "description": "Is a specialized model trained on medical literature and clinical notes to assist with medical queries and clinical decision-making.",
     "condition": "Use this adapter when users ask about medical information, diagnoses, or treatment options."},
    {"name": "leetcode",
     "description": "Is a model fine-tuned on competitive programming problems and solutions from LeetCode.",
     "condition": "Use this adapter when users ask for help with programming or need explanations of LeetCode problems, all messages related to this model starts with <human>:",
     "examples": [
         {"inputs": "<human>: Can you help me solve the two-sum problem on LeetCode?",
          "name": "leetcode"},
         {"inputs": "<human>: What is the best way to implement a binary search algorithm?",
          "name": "leetcode"},
         {"inputs": "<human>: Explain how to find the longest common subsequence in two strings.",
          "name": "leetcode"},
         {"inputs": "<human>: How can I optimize my solution for the 'median of two sorted arrays' problem?",
          "name": "leetcode"}
     ],
     },
    {
        "name": "exam",
        "description": "Is a model designed to assist with exam preparation, offering explanations and solutions for various academic subjects.",
        "condition": "Use this adapter when users need help with exam preparation in school or other study, including practice questions and study tips, all messages related to this model starts with <human>:",
        "examples": [
            {
                "inputs": "<human>: Premise: 'Three camels are carrying passengers through a desert.' Hypothesis: 'Three camels carry bedouins through the desert to an oasis.' Do we know that the hypothesis entailed by the premise? Plus step-by-step reasons.",
                "name": "exam"},
            {
                "inputs": "<human>: If 40% of the 880 students at a certain college are enrolled in biology classes, how many students at the college are not enrolled in a biology class? Help me solve this step by step.",
                "name": "exam"},
            {
                "inputs": "<human>: If s = { 8, 16, 24, 32, 40, 48 }, what is the product of mean and median of the numbers in s? Let's think step by step.",
                "name": "exam"},
        ],
    },
    {
        "name": "webgpt",
        "description": "Is a model capable of retrieving and summarizing information from the web in real-time.",
        "condition": "Use this adapter when users need up-to-date information or real-time web search capabilities.",
        "examples": [
            {"inputs": "Voiced by Harry Shearer, what Simpsons character was modeled after Ted Koppel?",
             "name": "webgpt"},
            {"inputs": "- The Straw man argument.\n\nPlease?", "name": "webgpt"},
            {"inputs": "Explain: Persistence of Evidence of Civilization", "name": "webgpt"},
            {"inputs": "In 1965, which Christmas song became the first song to be broadcast from space?",
             "name": "webgpt"},
            {"inputs": "Why is Starcraft so damn popular in Korea?\n\nWhy not, say, in China or other countries?",
             "name": "webgpt"},
            {"inputs": "Could you live off breast milk alone?", "name": "webgpt"},
            {"inputs": "How to start investing", "name": "webgpt"}
        ],
        # "keywords": [
        #     "web search", "real-time information", "news", "summaries",
        #     "recent events", "web data", "facts", "retrieval", "up-to-date"
        # ]
    },
    {
        "name": "gpt4tools",
        "description": "It generates human-like text and uses tools to indirectly understand images.",
        "condition": "Use this adapter when users need comprehensive answers about image that may require the use of multiple external tools."
    },
    {
        "name": "cot",
        "description": "Is a model specialized in generating chain-of-thought reasoning to provide detailed and step-by-step explanations.",
        "condition": "Use this adapter when users need detailed explanations or step-by-step reasoning for complex queries.",
        "examples": [
            {
                "inputs": "Q: Which of the following sentences is nonsensical?\nOptions:\n- Sentence A: \"He took his bicycle to the doctor for repair\"\n- Sentence B: \"He took his bicycle to the mechanic for repair\"\n\nLet's solve this gradually.",
                "name": "cot"
            },
            {
                "inputs": "Imagine a question and stream-of-consciousness explanation for which this is the answer: Sentence B",
                "name": "cot"
            },
            {
                "inputs": "Student: Given the sentence \"A young woman with blond-hair and a pink dior t-shirt checking under the cash drawer.\" is it true that \"A woman is looking under a drawer.\"?.\nTeacher: Let's think:",
                "name": "cot"
            }
        ],
        # "keywords": [
        #     "chain-of-thought", "reasoning", "step-by-step explanations", "logical processes",
        #     "multi-step solutions", "detailed explanations"
        # ]
    },
    {
        "name": "stackoverflow",
        "description": "Is a model trained on a wide range of programming and technical questions from StackOverflow.",
        "condition": "Use this adapter when users need help with programming questions, debugging, or technical issues.",
        "examples": [
            {
                "inputs": "The conversation between human and AI assistant.\n[|Human|] ",
                "name": "stackoverflow"
            },
            {
                "inputs": "The conversation between human and AI assistant.\n[|Human|] I'm interested in learning how to type hint in Python. Can you explain it to me?\n[|AI|] Sure! Type hints are a way to specify the expected data type of a variable, argument or return value in a function or method. This helps make your code more readable and helps prevent errors during runtime.\n[|Human|] ",
                "name": "stackoverflow"
            },
            {
                "inputs": "The conversation between human and AI assistant.\n[|Human|] I'm interested in learning more about regular expression compilers.\n[|AI|] Sure, I'd be happy to tell you about them. What do you specifically want to know?\n[|Human|] ",
                "name": "stackoverflow"
            },
        ],
        # "keywords": [
        #     "programming", "debugging", "technical issues", "coding problems", "StackOverflow",
        #     "JavaScript", "Python", "regular expressions", "OpenCV", "type hints"
        # ]
    }
]
