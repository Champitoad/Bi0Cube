<!DOCTYPE html>
<html>
    <head>
        <title>Bi0cube</title>
        <meta charset="utf-8" />
        <script type="text/javascript" src="biocube.js"></script>
    </head>

    <body onload="reloadSensors()">
        
        <h2>Capteurs :</h2>

        <div id="sensors">
            <p>Loading sensors values...</p>
        </div>

        <br><input id="refresh" type="button" value="Rafraîchir" onclick="reloadSensors()" /><br><br>


        <h2>Paramètres :</h2>
        
        <?php 
        try
        {
            $db = new PDO("mysql:host=127.0.0.1;dbname=bioduino", "root", "ppebi0cube");
        }
        catch(Exception $e)
        {
            die("Erreur : ".$e->getMessage());
        }

        $response = $db->query("SELECT * FROM Parameters");
        while($datas = $response->fetch())
        {
            $parameters[] = $datas["Value"];
        }
        $response->closeCursor();
        ?>

        <p>
            Température :
            <input id="temp" type="number" value="<?php echo($parameters[0]) ?>" /><br>
            Luminosité :
            <input id="lum" type="number" value="<?php echo($parameters[1]) ?>" /><br>
            Taux d'humidité : 
            <input id="hum" type="number" value="<?php echo($parameters[2]) ?>" /><br>
            Taux d'oxygène :
            <input id="O2" type="number" value="<?php echo($parameters[3]) ?>" /><br>
            Taux de dioxyde de carbone :
            <input id="CO2" type="number" value="<?php echo($parameters[4]) ?>" /><br>
        </p>

        <input id="save" type="button" value="Enregistrer" onclick="saveParameters()" /><br><br>


        <h2>Tests :</h2>

        <input id="test_leds" type="button" value="Test LEDs" onclick="testLeds()" /><br><br>


        <div>
            <input id="res_on" type="button" value="Résistance ON" onclick="res('on')" /><br>
            <input id="res_off" type="button" value="Résistance OFF" onclick="res('off')" />
        </div>

        <div>
            <input id="ventilo_on" type="button" value="Ventilo ON" onclick="ventilo('on')" /><br>
            <input id="ventilo_off" type="button" value="Ventilo OFF" onclick="ventilo('off')" />
        </div>

        <br>

        <div style="float: left">
            <input id="prod_o2_on" type="button" value="Prod O2 ON" onclick="prod_o2('on')" /><br>
            <input id="prod_o2_off" type="button" value="Prod O2 OFF" onclick="prod_o2('off')" />
        </div>

        <div style="float: left">
            <input id="prod_co2_on" type="button" value="Prod CO2 ON" onclick="prod_co2('on')" /><br>
            <input id="prod_co2_off" type="button" value="Prod CO2 OFF" onclick="prod_co2('off')" />
        </div>

        <div style="float: left">
            <input id="capt_o2_on" type="button" value="Capt O2 ON" onclick="capt_o2('on')" /><br>
            <input id="capt_o2_off" type="button" value="Capt O2 OFF" onclick="capt_o2('off')" />
        </div>

        <div style="float: left">
            <input id="capt_co2_on" type="button" value="Capt CO2 ON" onclick="capt_co2('on')" /><br>
            <input id="capt_co2_off" type="button" value="Capt CO2 OFF" onclick="capt_co2('off')" />
        </div>

        <div style="float: left">
            <input id="dechets_o2_on" type="button" value="Déchets O2 ON" onclick="dechets_o2('on')" /><br>
            <input id="dechets_o2_off" type="button" value="Déchets O2 OFF" onclick="dechets_o2('off')" />
        </div>

        <div style="float: left">
            <input id="dechets_co2_on" type="button" value="Déchets CO2 ON" onclick="dechets_co2('on')" /><br>
            <input id="dechets_co2_off" type="button" value="Déchets CO2 OFF" onclick="dechets_co2('off')" />
        </div>

    </body>
</html>
