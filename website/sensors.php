<?php
try
{
    $db = new PDO("mysql:host=127.0.0.1;dbname=bioduino", "root", "ppebi0cube");
}
catch(Exception $e)
{
    die("Erreur : ".$e->getMessage());
}

$response = $db->query("SELECT * FROM Sensors");
while($datas = $response->fetch())
{
    if($datas["Sensor"] == "temp")
        echo("Température : {$datas["Value"]}<br>");
    if($datas["Sensor"] == "lum")
        echo("Luminosité : {$datas["Value"]}<br>");
    if($datas["Sensor"] == "hum")
        echo("Taux d'humidité : {$datas["Value"]}<br>");
    if($datas["Sensor"] == "O2")
        echo("Taux d'oxygène : {$datas["Value"]}<br>");
    if($datas["Sensor"] == "CO2")
        echo("Taux de dioxyde de carbone : {$datas["Value"]}<br>");
}
$response->closeCursor();
?>
