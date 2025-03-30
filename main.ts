function converOjosama(text: String): string {
  const rules: { [pattern: string]: string } = {
    "ですかしら": "でございますかしら",
    "ますかしら": "でございますかしら",
    "ですね": "でございますわね",
    "ますね": "でございますわね",
    "ですよ": "でございますわよ",
    "ますよ": "でございますわよ",
    "ですか": "でございますかしら",
    "ますか": "でございますかしら",
    "です": "でございますわ",
    "ます": "でございますわ",
  };

  return text.replace(/ですかしら|ますかしら|ですね|ますね|ですよ|ますよ|ですか|ますか|です|ます/g, (match) => {
    return rules[match] || match;
  });
}

const input: string = "今日はいい天気ですね。散歩しますか？";
const result: string = converOjosama(input);
console.log(result);
