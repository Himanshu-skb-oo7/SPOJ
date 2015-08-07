<?php
 
for(;;) {
  $input = trim(fgets(STDIN));
  if ($input != 42) {
    echo $input , "\n";
  } else {
    break;
  }
} 
