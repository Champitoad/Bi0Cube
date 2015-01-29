var req;
try {
    req = new XMLHttpRequest();
} catch (e) {
    alert("No AJAX Support");
    return;
}



function reloadSensors()
{
    document.getElementById("refresh").disabled = true;

    url = "sensors.php";

    req.onreadystatechange = processReqChange("sensors");
    req.open("GET", url, true);
    req.send(null);
}

function saveParameters()
{
    document.getElementById("save").disabled = true;

    var temp = document.getElementById("temp").value;
    var lum = document.getElementById("lum").value;
    var hum = document.getElementById("hum").value;
    var O2 = document.getElementById("O2").value;
    var CO2 = document.getElementById("CO2").value;

    url = "parameters.php?temp=" + temp + "&lum=" + lum + "&hum=" + hum + "&O2=" + O2 + "&CO2=" + CO2;

    req.onreadystatechange = processReqChange("parameters");
    req.open("GET", url, true);
    req.send(null);
}



// ***** TESTS MODULE LUMINOSITE *****


function testLeds()
{
    document.getElementById("test_leds").disabled = true;

    url = "tests/test_leds.php";

    req.onreadystatechange = processReqChange("test_leds");
    req.open("GET", url, true);
    req.send(null);
}



// ***** TESTS MODULE TEMPERATURE *****


function res(state)
{
    document.getElementById("res_on").disabled = true;
    document.getElementById("res_off").disabled = true;

    url = "tests/res_" + state + ".php";

    req.onreadystatechange = processReqChange("res_" + state);
    req.open("GET", url, true);
    req.send(null);
}

function ventilo(state)
{
    document.getElementById("ventilo_on").disabled = true;
    document.getElementById("ventilo_off").disabled = true;

    url = "tests/ventilo_" + state + ".php";

    req.onreadystatechange = processReqChange("ventilo_" + state);
    req.open("GET", url, true);
    req.send(null);
}



// ***** TESTS MODULE ATMOSPHERE *****


function prod_o2(state)
{
    document.getElementById("prod_o2_on").disabled = true;
    document.getElementById("prod_o2_off").disabled = true;

    url = "tests/prod_o2_" + state + ".php";

    req.onreadystatechange = processReqChange("prod_o2_" + state);
    req.open("GET", url, true);
    req.send(null);
}

function prod_co2(state)
{
    document.getElementById("prod_co2_on").disabled = true;
    document.getElementById("prod_co2_off").disabled = true;

    url = "tests/prod_co2_" + state + ".php";

    req.onreadystatechange = processReqChange("prod_co2_" + state);
    req.open("GET", url, true);
    req.send(null);
}

function capt_o2(state)
{
    document.getElementById("capt_o2_on").disabled = true;
    document.getElementById("capt_o2_off").disabled = true;

    url = "tests/capt_o2_" + state + ".php";

    req.onreadystatechange = processReqChange("capt_o2_" + state);
    req.open("GET", url, true);
    req.send(null);
}

function capt_co2(state)
{
    document.getElementById("capt_co2_on").disabled = true;
    document.getElementById("capt_co2_off").disabled = true;

    url = "tests/capt_co2_" + state + ".php";

    req.onreadystatechange = processReqChange("capt_co2_" + state);
    req.open("GET", url, true);
    req.send(null);
}

function dechets_o2(state)
{
    document.getElementById("dechets_o2_on").disabled = true;
    document.getElementById("dechets_o2_off").disabled = true;

    url = "tests/dechets_o2_" + state + ".php";

    req.onreadystatechange = processReqChange("dechets_o2_" + state);
    req.open("GET", url, true);
    req.send(null);
}

function dechets_co2(state)
{
    document.getElementById("dechets_co2_on").disabled = true;
    document.getElementById("dechets_co2_off").disabled = true;

    url = "tests/dechets_co2_" + state + ".php";

    req.onreadystatechange = processReqChange("dechets_co2_" + state);
    req.open("GET", url, true);
    req.send(null);
}



function processReqChange(id)
{
    return function()
    {
        if(req.readyState == 4)
        {
            if(req.status == 200)
            {
                switch(id)
                {
                    case "sensors":
                        document.getElementById("sensors").innerHTML = req.responseText;
                        document.getElementById("refresh").disabled = false;
                        break;
                    case "parameters":
                        document.getElementById("save").disabled = false;
                        break;


                    case "test_leds":
                        document.getElementById("test_leds").disabled = false;
                        alert("Test des LEDs terminé !");
                        break;


                    case "res_on":
                        document.getElementById("res_off").disabled = false;
                        break;
                    case "res_off":
                        document.getElementById("res_on").disabled = false;
                        break;

                    case "ventilo_on":
                        document.getElementById("ventilo_off").disabled = false;
                        break;
                    case "ventilo_off":
                        document.getElementById("ventilo_on").disabled = false;
                        break;


                    case "prod_o2_on" :
                        document.getElementById("prod_o2_off").disabled = false;
                        break;
                    case "prod_o2_off" :
                        document.getElementById("prod_o2_on").disabled = false;
                        break;
                    case "prod_co2_on" :
                        document.getElementById("prod_co2_off").disabled = false;
                        break;
                    case "prod_co2_off" :
                        document.getElementById("prod_co2_on").disabled = false;
                        break;

                    case "capt_o2_on" :
                        document.getElementById("capt_o2_off").disabled = false;
                        break;
                    case "capt_o2_off" :
                        document.getElementById("capt_o2_on").disabled = false;
                        break;
                    case "capt_co2_on" :
                        document.getElementById("capt_co2_off").disabled = false;
                        break;
                    case "capt_co2_off" :
                        document.getElementById("capt_co2_on").disabled = false;
                        break;

                    case "dechets_o2_on" :
                        document.getElementById("dechets_o2_off").disabled = false;
                        break;
                    case "dechets_o2_off" :
                        document.getElementById("dechets_o2_on").disabled = false;
                        break;
                    case "dechets_co2_on" :
                        document.getElementById("dechets_co2_off").disabled = false;
                        break;
                    case "dechets_co2_off" :
                        document.getElementById("dechets_co2_on").disabled = false;
                        break;
                    default:
                        break;
                }
            }
            else
            {
                alert("There was a problem during the request: " + req.statusText);
            }
        }
    }
}
