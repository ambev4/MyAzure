
# Resource group do projeto
resource "azurerm_resource_group" "myazure_rg" {
  name     = "myazure_rg"
  location = var.myazure_location
}

# Criação do ambiente de container apps
resource "azurerm_container_app_environment" "myazure_app_env" {
  name                = "myazure-app-env"
  location            = var.myazure_location
  resource_group_name = azurerm_resource_group.myazure_rg.name
}

# Criação do container de backend
resource "azurerm_container_app" "myazure_app_backend" {
  name                         = "myazure-app-backend"
  container_app_environment_id = azurerm_container_app_environment.myazure_app_env.id
  resource_group_name          = azurerm_resource_group.myazure_rg.name
  revision_mode                = "Single"

  template {
    container {
      name   = "myazure-app-backend"
      image  = "ambev4/lab1:myazure-backend"
      cpu    = 0.25
      memory = "0.5Gi"
    }
  }

  ingress {
    allow_insecure_connections = true
    external_enabled           = false
    target_port                = 8000
    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }
}

# Criação do container Nginx com as imagens estáticas
resource "azurerm_container_app" "myazure_app_nginx" {
  name                         = "myazure-app-nginx"
  container_app_environment_id = azurerm_container_app_environment.myazure_app_env.id
  resource_group_name          = azurerm_resource_group.myazure_rg.name
  revision_mode                = "Single"

  template {
    container {
      name   = "myazure-app-nginx"
      image  = "ambev4/lab1:myazure-nginx"
      cpu    = 0.25
      memory = "0.5Gi"
    }
  }

  ingress {
    allow_insecure_connections = true
    external_enabled           = true
    target_port                = 80
    traffic_weight {
      percentage      = 100
      latest_revision = true
    }
  }
}