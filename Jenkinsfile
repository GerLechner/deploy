node {
    
    stage('Git Clone'){
        git credentialsId: 'GIT_CREDENTIALS', url: 'https://github.com/GerLechner/deploy'
    }
    
    stage('Build Docker Image'){
        sh "docker build -t glechner99/proyecto-final ."
    }
    
    
    stage('Push Docker Image') {
        withCredentials([string(credentialsId: 'DOCKER_CREDENTIALS', variable: 'DOCKER_CREDENTIALS')]) {
            sh "docker login -u glechner99 -p ${DOCKER_CREDENTIALS}"
        }
        sh "docker push glechner99/proyecto-final"
    }
    
   
    stage('Deploy Kubernetes'){
        withCredentials([string(credentialsId: 'IP_PRODUCCION', variable: 'IP_PRODU'), string(credentialsId: 'USER_PRODUCCION', variable: 'USER_PRODU')]) {

            def produccion = "${USER_PRODU}@${IP_PRODU}"


            sh(script: "ssh ${produccion} 'minikube start'")
            sh(script: "ssh ${produccion} 'kubectl delete service deploy-proyecto-final'")
            sh(script: "ssh ${produccion} 'kubectl delete deployment deploy-proyecto-final'")


            sh(script: "ssh ${produccion} 'kubectl create deployment deploy-proyecto-final --image=glechner99/proyecto-final'")
            sh(script: "ssh ${produccion} 'kubectl expose deployment deploy-proyecto-final --port=5000 --type=LoadBalancer'")


            //sleep(time:10, unit: "SECONDS")
            sh(script: "ssh ${produccion} 'minikube service deploy-proyecto-final --url'")


            def minikubeIp = sh(script:"ssh ${produccion} 'minikube ip'", returnStdout: true).trim()
            def puerto = sh(script:"ssh ${produccion} 'kubectl get service deploy-proyecto-final --output='jsonpath={.spec.ports[0].nodePort}' --namespace=default'", returnStdout: true).trim()

            sh(script: "echo ssh -L 192.168.192.130:${puerto}:${minikubeIp}:${puerto}")

        }
    }
}
