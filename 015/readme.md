# MISSION 015

```
$ python3 decode.py

<?php

if (!isset($_GET['password']) || !is_string($_GET['password'])) {
  die("bad password");
}

$p = $_GET['password'];

if (strlen($p) !== 25) {
  die("bad password");
}

if (md5($p) !== 'e66c97b8837d0328f3e5522ebb058f85') {
  die("bad password");
}

// Split the password in five and check the pieces.
// We need to be sure!
$values = array(
  0 => 'e6d9fe6df8fd2a07ca6636729d4a615a',
  5 => '273e97dc41693b152c71715d099a1049',
  10 => 'bd014fafb6f235929c73a6e9d5f1e458',
  15 => 'ab892a96d92d434432d23429483c0a39',
  20 => 'b56a807858d5948a4e4604c117a62c2d'
);

for ($i = 0; $i < 25; $i += 5) {
  if (md5(substr($p, $i, 5)) !== $values[$i]) {
    die("bad password");
  }
}

die("GW!");
```

```
$ john hashes.txt --format=raw-md5

[ after ~ 5 minutes ]

$ john hashes.txt --format=raw-md5 --show
1:Pie c
2:harts
4:delic
5:ious!
```

The third hash could be easily guessed from the content:

```
$ echo -n ' are ' | md5sum
bd014fafb6f235929c73a6e9d5f1e458

$ echo -n 'Pie charts are delicious!' | md5sum
e66c97b8837d0328f3e5522ebb058f85
```
