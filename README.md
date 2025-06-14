📘 Exercise 2.1 – Connecting Pods via HTTP
This exercise demonstrates how to connect two Kubernetes pods (pingpong and log-output) using HTTP communication instead of shared volumes.

🧱 Project Structure
lua
Copy
Edit
.
├── manifests
│   ├── pingpong-deployment.yaml
│   ├── pingpong-service.yaml
│   ├── log-output-deployment.yaml
│   └── log-output-service.yaml
├── pingpong
│   └── index.js
├── log-output
│   └── index.js
├── Dockerfile.pingpong
├── Dockerfile.log-output
├── README.md
🚀 Functionality
Pingpong App keeps track of the number of times it has been "pinged".

Log Output App makes an HTTP GET request to the Pingpong app, retrieves the ping count, and prints a UUID and timestamp along with the ping count.

Example output from log-output:

yaml
Copy
Edit
2024-06-08T12:30:45.123Z: 9f123abc-b7e1-4a90-b123-abcde4567890
Ping / Pongs: 3
🐳 Docker Instructions
Make sure both apps are built and pushed to your Docker Hub account.

1. Build and push images
Replace samyak2605 with your Docker Hub username if needed.

bash
Copy
Edit
# Pingpong
docker build -t samyak2605/pingpong-app -f Dockerfile.pingpong .
docker push samyak2605/pingpong-app

# Log Output
docker build -t samyak2605/log-output-app -f Dockerfile.log-output .
docker push samyak2605/log-output-app
☸️ Kubernetes Setup
2. Apply manifests
bash
Copy
Edit
kubectl apply -f manifests/pingpong-deployment.yaml
kubectl apply -f manifests/pingpong-service.yaml
kubectl apply -f manifests/log-output-deployment.yaml
kubectl apply -f manifests/log-output-service.yaml
3. Verify pods
bash
Copy
Edit
kubectl get pods
Ensure both pingpong and log-output pods are in Running status.

🌐 Access the App
4. Port forward the log-output service
bash
Copy
Edit
kubectl port-forward service/log-output-service 3000:3000
5. Open browser
Navigate to:

arduino
Copy
Edit
http://localhost:3000
You should see a line with timestamp, UUID, and current ping count.

🛠 Tech Stack
Node.js (Express)

Kubernetes

Docker

🧪 Troubleshooting
ImagePullBackOff: Make sure the image is correctly built and pushed to Docker Hub.

CrashLoopBackOff: Check your app logs using:

bash
Copy
Edit
kubectl logs <pod-name>
