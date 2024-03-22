<?php
$url = 'http://localhost:8080/api';
$response = file_get_contents($url);

if ($response !== false) {
    echo $response;
    echo "\n";
} else {
    echo "failed";
}
?>
