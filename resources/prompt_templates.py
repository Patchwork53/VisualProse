summary_extraction_instruction_key = (
    "What is this article about? Answer in 1-2 sentences. Respond in English. Answer in JSON format with a key 'summary', and summary as the the value.",
    "summary"
)
core_message_extraction_instruction_key = (
    "What is the core message of the article above? Answer in 1-2 sentences. Respond in English. Answer in JSON format with a key 'core_message', and core message as the value.",
    "core_message"
)

abstract_depiction_instruction_key = (
"""
You are a philosophy and design student tasked with coming up with thought provoking depictions of articles. The depictions and illustrations must not be on the nose or simple repetition of entities in the topic. Use metaphors and allegories whenever you can. The prompt should be simple, succinct but also make the viewer think!

Artstyle Instructions:

1. Do not suggest hyper-realistic depictions.
2. If the depiction includes people, always make it animated and cartoonized.
3. End with tone setting works like "dark", "moody" or "cozy", "warm" when applicable
4. The prompt should be as as short and simple as possible. So simple that even a child can understand it.
5. The prompt must definitely never exceed one line

Here's a few examples.

[
    {
        "article_topic": "The author strategically married an older man while in her early 20s to take advantage of her youth and beauty, prioritizing ease over fairness in navigating the challenges faced by women.",

        "abstract_depiction": "An empty chessboard with a single black queen piece and a gold king piece."
    },

    {
        "article_topic": "The core message of the article is that Taylor Swift has reached a point of "over-saturation" in her career, where her immense success and privilege have made her a figurehead for broader societal frustrations and conversations, particularly those related to race, gender, and the limitations of white women's progressive politics. The article suggests that Swift is grappling with this reality and may be moving beyond trying to fit into the constraining role of the "good girl" in order to navigate her cultural significance and the challenges that come with it.",

        "abstract_depiction": "a female pop star in a glass box singing and dancing at peace with eyes closed and an audience outside, cartoon, animated"
    },

    {
        "article_topic": "The core message of this article is that the resurgence of the "America First" movement and Donald Trump's likely nomination as the Republican candidate in the 2024 US presidential election pose a serious threat to American leadership and global stability. The article argues that if Trump wins, it would undermine US national security interests and bring about a chaotic world reminiscent of the 1930s. It also highlights the contrast between Biden's well-funded campaign and his challenges in maintaining a broad coalition, particularly among younger, progressive voters who are critical of his handling of the war in Gaza.",

        "abstract_depiction": "a bald eagle nose diving straight into a stormy sea."
    },

    {
        "article_topic": "The core message of this article is that Dune: Part Two delves deeper into the darker aspects of Paul Atreides' transformation into a mythic figure, challenging the notion of him as a straightforward hero. The film emphasizes the complicated nature of Paul's journey, the role of the Fremen, especially the women, in the revolution against their oppressors, and the dangerous implications of the idea of a "chosen one" or messiah figure. While acknowledging the visually stunning and masterfully crafted elements of the film, the article also points out the problematic aspects of the white savior narrative and the limited roles given to Muslim and MENA actors.",

        "abstract_depiction": "abstract depiction of a false prophet"
    },

    {
        "article_topic": "The article explains the concept of a "third place" - a public space outside of home and work where people can relax, socialize, and feel a sense of community, which is crucial for combating the growing epidemic of loneliness and isolation in modern society.",

        "abstract_depiction":"A social event with faceless adults and kids, all connected together by thin golden threads, animated, cartoon, warm, cozy"
    },
        
    {
        "article_topic": "The article criticizes Luca Guadagnino's film "Call Me by Your Name" for its shallow storytelling despite its progressive depiction of a same-sex relationship. It argues that the film focuses on aesthetics and superficiality, neglecting character development, dialogue, and exploration of the characters' inner lives and experiences. Luca Guadagnino's "Call Me by Your Name" is a superficially charming film that lacks depth and intimacy due to its lack of character development, dialogue, and cinematic technique.",

        "abstract_depiction":"A beautiful young man sitting on a chair in a scenic Italian landscape, surrounded by flowers and leaves, but his face is obscured by a blank mask, cartoon, animated"
    }
]

Answer in a single JSON with the key 'abstract_depiction'.""", "abstract_depiction"
)
