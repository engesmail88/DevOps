# Build Image From Docker File
docker build -t website-img .

# List Images
docker images

# Build Container From The Image
docker run -d --name website-container -p 8000:80 website-img

# Browse The Website http://localhost:8000

