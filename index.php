<!DOCTYPE html>
<html lang="fr">
    <head>
		<title> PHP / MySQL</title>
        <meta charset="utf-8">
		<link rel="stylesheet" href="style/style.css" />
	</head>
	<body>
    <?php
        require('config.php');
		session_start();
        if (isset($_POST['words'])){	
			$mots = stripslashes($_REQUEST['words']);
			$mots = mysqli_real_escape_string($conn, $mots);
			$query = 'SELECT * FROM liste_mots WHERE words LIKE "%' . $mots . '%" ';
			//"SELECT * FROM `liste_mots` WHERE mots = '" .$mots. "'";
			
			$result = mysqli_query($conn,$query) or die(mysql_error());
			$rows = mysqli_num_rows($result);
			if($rows === 0){
				$message = "Le mots que vous recherchez n'est existe pas.";
			}
		}
    ?>
    <form class="box" action="" method="post">
			<div class="typing-demo">
				<h1 class="box-login">MySearch</h1>
			</div>
			<input type="text" class="box-input" name="words" placeholder="Search ">
			<input class= "button-submit" type="submit" value=" " name="submit" >
			<?php if(! empty($rows) ) { ?>
				<table>
					<?php while($row = $result->fetch_assoc()) { ?>					

						<tr>
							<td><?php echo $row['words'] ;?></td>	
							<td><?php echo "occurrence (",$row['number_of_words'],")" ;?></td>		
							<td>
								<a href="./python/file/<?php echo $row['file_name'];?>" target="_blank"><?php echo $row['file_name'];?></a>
							</td>
						</tr>
					<?php } }?>
				</table>
			<?php if(! empty($message)) { ?>
				<p class="errorMessage"><?php echo $message; ?></p>
			<?php } ?>
		</form>
	</body>
</html>
