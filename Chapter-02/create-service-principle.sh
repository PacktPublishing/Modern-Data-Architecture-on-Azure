subscriptionsid=$(az account show --query id -o tsv)
az ad sp create-for-rbac \
--name sp-idp-dataaccess-principal \
--role "Contributor" \
--scopes /subscriptions/$subscriptionsid

