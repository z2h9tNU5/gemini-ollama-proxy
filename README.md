# ビルド
```
docker build -t gemini-openai-proxy .
```


# 実行
```
docker run -p 11434:11434 \
  -e GOOGLE_API_KEY=your_api_key \
  -e MODEL_NAME=gemini-3-flash-preview \
  gemini-openai-proxy
```