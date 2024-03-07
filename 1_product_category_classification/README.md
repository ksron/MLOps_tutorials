# 1. [Environment Setup] Real-time Product Category Classification

Setting up an environment for real-time product category classification.

## Project Background for using MLOps

1. **Continuous influx of product data**: To handle all in real-time demands substantial GPU utilization.
2. **GPU costs**: GPU occupancy be minimized during low traffic + enabling near real-time processing?
3. **Unified Platform** for deployment of models from ML researchers using PyTorch and TensorFlow.
4. **Model management**: Includes model storage, versioning of deployed models, and deployment history.
5. **Failure management**: Automating model deployment to prevent human errors, streamlining deployment processes, and addressing failures in model APIs.

## Tools

1. Google Kubernetes Engne(GKE) & Kubernetes
    - Also uses cloud disk of 10GB
2. KServe: Model inference platform on top of k8s
    - supports:
        - standard API for diffent ML protols
        - efficient resource management using autoscaling (enables autoscaling to 0)
    - Installation: [KServe Installation Page](https://kserve.github.io/website/master/admin/serverless/serverless/#1-install-knative-serving)
3. Knative 
    - supports:
        - platform for serverless application deployment & management
        - autoscaling based on the traffic (-> 0)
        - Optimizing resource cost
    - Installation: [Knative Installation](https://knative.dev/docs/install/)
4. Istio: Platform for service mesh
    - supports:
        - network connection management for each app in microservice distributed environment
        - provides stable service and traffic management
    - Installation: [Installing Istio for Knative](https://knative.dev/docs/install/installing-istio/#using-istio-mtls-feature-with-knative), [Istioctl](https://istio.io/latest/docs/setup/install/istioctl/)
5. Cert-manager: cert. management for HTTP communication
    - Installation: [cert-manager installation](https://cert-manager.io/docs/installation/)
