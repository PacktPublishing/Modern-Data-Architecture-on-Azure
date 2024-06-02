rg_name="rg-idpCosmosdbRG"
user_assigned_identity_name="idp-dataaccess-user-assigned-identity"
az identity create -g $rg_name -n $user_assigned_identity_name

az identity list -g $rg_name

