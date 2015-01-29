<?php
try
{
    $db = new PDO("mysql:host=127.0.0.1;dbname=bioduino", "root", "ppebi0cube");
}
catch(Exception $e)
{
    die("Erreur : ".$e->getMessage());
}

$db->exec("UPDATE Parameters SET Value = ".$_GET["temp"]." WHERE Parameter = 'temp'");
$db->exec("UPDATE Parameters SET Value = ".$_GET["lum"]." WHERE Parameter = 'lum'");
$db->exec("UPDATE Parameters SET Value = ".$_GET["hum"]." WHERE Parameter = 'hum'");
$db->exec("UPDATE Parameters SET Value = ".$_GET["O2"]." WHERE Parameter = 'O2'");
$db->exec("UPDATE Parameters SET Value = ".$_GET["CO2"]." WHERE Parameter = 'CO2'");
?>
