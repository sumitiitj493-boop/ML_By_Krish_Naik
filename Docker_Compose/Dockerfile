# 1. Base image (Python + Alpine = lightweight)
FROM python:3.7-alpine

# 2. Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0


# 3. Set working directory inside container
WORKDIR /code

# 4. Copy project files into container
COPY . .

# 5. Install dependencies
# (FIX: -r ke baad space hona chahiye)
RUN pip install --no-cache-dir -r requirements.txt

# 6. Expose Flask port
EXPOSE 5000

# 7. Run the Flask application
CMD ["flask", "run"]
