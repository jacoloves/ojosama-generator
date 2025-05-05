import MeCab

word_dict = {
    "私": "わたくし",
    "僕": "わたくし",
    "俺": "わたくし",
    "あなた": "おまえさま",
    "本": "ご本",
    "読む": "お読みになる",
    "好き": "お気に召す",
    "食べる": "お召し上がりになる",
    "猫": "猫ちゃん",
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
