FROM python:3.12-slim

# 不要ファイル削減 & 高速化
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 依存関係だけ先にコピー（キャッシュ最適化）
COPY pyproject.toml ./

# pip 最小構成でインストール
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir .

# アプリ本体
COPY main.py ./

EXPOSE 11434

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "11434"]
