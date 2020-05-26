set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
	[
	    r"(.*)name",
		["I'm chatbot"]
	],
    [
        r"what is your name?|what's your name|your name?",
        ["You can call me a chatbot ",]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"I am fine(.*)",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"how can i help you? ",
        ["i am looking for online guides and courses to learn data science, can you suggest?", "i am looking for data science training platforms",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear","How can i help you?:)",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["Iam happy to help", "No problem, you're welcome",]
    ],
    [
        r"quit",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
