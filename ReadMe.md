
virtual environment

python3 -m venv GenAI_venv
source GenAI_venv/bin/activate


minikube stop

minikube start
minikube status


to check on mini kube nodes made or not
kubectl get all

to access app on minikube
minikube service mylb



to run workflow just commmit to github
git add .
git commit -m "updated the main code a little"
git push origin main