<!DOCTYPE html>
<html lang="fr">
    <head>
        <title> PHP / MySQL</title>
        <meta charset="utf-8">
    </head>
    <body>
      
        <?php
            define('SERVER_NAME_01', 'localhost');
            define('USERNAME_02' ,'python3');
            define('PASSWORD_03','python3');
            define('DB_NAME_04' , 'File');
            //On établit la connexion
            $conn = new mysqli(SERVER_NAME_01, USERNAME_02, PASSWORD_03,DB_NAME_04);
            //On vérifie la connexion
            if($conn->connect_error){
                die('Erreur : ' .$conn->connect_error); 
            }
        ?>
    </body>
</html>