function converOjosama(text: String): string {
  const wordDictionary: { [key: string]: string } = {
    "私": "わたくし",
    "僕": "わたくし",
    "俺": "わたくし",
    "あなた": "おまえさま",
    "君": "おまえさま",
    "家": "お屋敷",
    "本": "ご本",
    "ご飯": "お食事",
    "学校": "お学校",
    "猫": "猫ちゃん",
  };

  const phraseRules: { [pattern: string]: string } = {
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

  const phraseConverted = text.replace(
    /ですかしら|ますかしら|ですね|ますね|ですよ|ますよ|ですか|ますか|です|ます/g,
    (match) => phraseRules[match] || match
  );

  const wordConverted = phraseConverted.replace(
    new RegExp(Object.keys(wordDictionary).join("|"), "g"),
    (match) => wordDictionary[match] || match
  );

  return wordConverted;
}

document.getElementById("convert")?.addEventListener("click", async () => {
  const input = (document.getElementById("input") as HTMLTextAreaElement).value;
  
  const response = await fetch("http://localhost:8000/convert", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: input }),
  });

  if (!response.ok) {
    alert("変換中にエラーが発生しましたわ！");
    return;
  }

  const data = await response.json();
  const output = document.getElementById("output");
  if (output) output.textContent = data.result;
});
