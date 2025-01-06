output "azurerm_container_app_url" {
  value = azurerm_container_app.myazure_app_nginx.latest_revision_fqdn
}