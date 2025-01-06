# locals {
#   default_tags = {
#     environment = var.env
#     owner       = "J.Son"
#     app         = var.app
#   }
# }


# Resource group do projeto
resource "azurerm_resource_group" "myazure_rg" {
  name     = "myazure_rg"
  location = var.myazure_location
}

# resource "azurerm_network_security_group" "myazure_sg1" {
#   name                = "myazure_sg1"
#   location            = var.myazure_location
#   resource_group_name = azurerm_resource_group.myazure_rg.name

#   security_rule {
#     name                       = "TCP_80"
#     priority                   = 100
#     direction                  = "Inbound"
#     access                     = "Allow"
#     protocol                   = "Tcp"
#     source_port_range          = "*"
#     destination_port_range     = "80"
#     source_address_prefix      = "*"
#     destination_address_prefix = "*"
#   }

#   tags = {
#     environment = "Production"
#   }
# }
# VNet do projeto
# resource "azurerm_virtual_network" "myazure_vnet" {
#   name                = "myazure_vnet"
#   resource_group_name = azurerm_resource_group.myazure_rg.name
#   location            = var.myazure_location
#   address_space       = ["10.0.0.0/16"]

#   subnet {
#   name             = "myazure_subnet"
#   address_prefixes = ["10.0.1.0/24"]
#   security_group   = azurerm_network_security_group.myazure_sg1.id
#   }

#   tags = {
#   environment = "Production"
#   }
# }

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