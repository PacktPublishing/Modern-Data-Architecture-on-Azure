rg_name="rg-idpCosmosdbRG"
primary_region="westus2"
secondary_region="westus"
az group create --name $rg_name --location $primary_region
az deployment group create --resource-group $rg_name --template-file create-cosmos-db.bicep --parameters primaryRegion=$primary_region secondaryRegion=$secondary_region