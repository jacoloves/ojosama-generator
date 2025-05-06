import MeCab

word_dict = {
    # noun
    "私": "わたくし",
    "僕": "わたくし",
    "俺": "わたくし",
    "あなた": "おまえさま",
    "本": "ご本",
    "猫": "猫ちゃん",

    # verb
    "読む": "お読みになります",
    "食べる": "お食べになる",
    "飲む": "お飲みになる",
    "行く": "おいでになる",
    "来る": "おいでになる",
    "する": "なさる",
    "見る": "ご覧になる",
    "聞く": "お聞きになる",
    "話す": "お話しになる",
    "買う": "お買いになる",
    "売る": "お売りになる",
    "教える": "お教えになる",

    # adjective
    "いい": "よろしい",
    "悪い": "よくない",
    "大きい": "大きい",
    "小さい": "小さい",
    "高い": "高い",
    "安い": "安い",
    "好き": "お気に召します",
    "嬉しい": "嬉しゅうございます",
    "楽しい": "楽しゅうございます",
    "美しい": "美しゅうございます",
}


def conver_ojousama(text: str) -> str:
    tagger = MeCab.Tagger("-r /opt/homebrew/etc/mecabrc")
    node = tagger.parseToNode(text)

    result = []

    while node:
        surface = node.surface
        features = node.feature.split(",")
        base_form = features[6] if len(features) > 6 else surface

        result.append(word_dict.get(base_form, surface))
        node = node.next

    return "".join(result)


# if __name__ == "__main__":
#    input_text = "私は本を読みます。あなたも本が好きですか？"
#    print(conver_ojousama(input_text))
