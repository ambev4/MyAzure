# Resource group do projeto
resource "azurerm_resource_group" "myazure_rg" {
  name     = "myazure_rg"
  location = var.myazure_location
}

# VNet do projeto
resource "azurerm_virtual_network" "myazure_vnet" {
  name                = "myazure_vnet"
  resource_group_name = azurerm_resource_group.myazure_rg.name
  location            = var.myazure_location
  address_space       = ["10.0.0.0/16"]
}

