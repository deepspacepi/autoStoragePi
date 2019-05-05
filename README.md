# autoStoragePi
Automatic storage machine based on Raspberry Pi

Αυτόματο σύστημα αποθήκευσης βασισμένο σε Raspberry Pi

Με την βοήθεια τριών Raspberry Pi και τον απαραίτητων αισθητήρων και κινητήρων θα δημιουργηθεί ένα αυτόματο σύστημα αποθήκευσης με τα εξής χαρακτηριστικά. Θα υλοποιηθού οι εξής αυτόματοι μηχανισμοί :
- Μηχανισμός Α οποίος θα μεταφέρει τα επόμενα αντικείμενα προς τοποθέτηση σε μία κυλιόμενη ράγα αλλά και θα παίρνει τα αντικείμενα που εξάγωνται από τον απθηκευτικό χώρο.
- Μηχανισμός Β ο οποίο θα παιρνει το αντικείμενο από την ράγα και θα το τοποθετεί σε ένα κενό ράφι. Ο ίδιος μηχανισμός θα παίρνει το αντικείμενο που ζητείται από το ράφι και θα το τοποθετεί στην κυλιόμενη μπάρα εξόδου.

Ένα παράδειγμα του μηχανισμού Β φαίνεται στο επόμενο βίντεο του Youtube. Στην υλοποίηση μας η κατασκευή θα γίνει σε μικροκλίμακα.
https://www.youtube.com/watch?v=QetS5n2ZE5k&t=109s

Στα επόμενα βίντεο φαίνεται παράδειγμα της δικής μας υλοποίησης.
https://www.youtube.com/watch?v=x4pSujQboqA
https://www.youtube.com/watch?v=gPdcfqCh67Y


Η υλοποίηση του προγραμματιστικού μέρους όσον αφορά τα Raspberry Pi θα γίνει σε γλώσσα Python η οποία είναι και πανελλαδικώς εξεταζόμενη στον Τομέα Πληροφορικής του ΕΠΑΛ. Η υλοποίηση του προγραμματιστικού μέρους για το κινητό τηλέφωνο θα γίνει σε AppInventor. Έχει επιλεγεί συνεργασία δύο Raspberry Pi για να πειραματιστούν οι μαθητές με την επικοινωνία και τον συγχρονισμό των συσκευών καθώς και με την δημιουργία μίας απλής βάσης δεδομένων όπου θα αποθηκευέται κάθε χρονική στιγμή η κατάσταση του αποθηκευτικού χώρου.

Απαιτούμενος εξοπλισμός είναι ο εξής :

<table>
  <tr>
    <td>Α/Α</td>
    <td>Ονομασία</td>
    <td>Ποσότητα</td>
    <td>Τιμή Τεμαχίου</td>
    <td>Συνολική Τιμή</td>
  </tr>
  <tr>
    <td>1</td>
    <td>
      Raspberry Pi 3 - Model B+</br>
      https://grobotronics.com/raspberry-pi-3-model-b-el.html
    </td>
    <td>1</td>
    <td>41,90 €</td>
    <td>41,90 €</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Κάρτα μνήμης microSDHC 16GB Class 10</br>
    https://grobotronics.com/microsdhc-16gb-class-10-sandisk-ultra-sdsquar-sdsquar-016g-gn6ma.html
    </td>
    <td>1</td>
    <td>8,90 €</td>
    <td>8,90 €</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Pimoroni Raspberry Pi Zero W Starter Kit</br>
    https://grobotronics.com/pimoroni-raspberry-pi-zero-w-starter-kit.html
    </td>
    <td>2</td>
    <td>42,90 €</td>
    <td>85,80 €</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Adafruit DC & Stepper Motor HAT for Raspberry Pi - Mini Kit
</br>
https://grobotronics.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi-mini-kit.html
</td>
    <td>1</td>
    <td>27,70 €</td>
    <td>27,70 €</td>
  </tr>
  <tr>
    <td>5</td>
    <td>
Adafruit 16-Channel PWM / Servo Bonnet for Raspberry Pi
</br>
https://grobotronics.com/adafruit-16-channel-pwm-servo-bonnet-for-raspberry-pi.html
</td>
    <td>1</td>
    <td>12,50 €</td>
    <td>12,50 €</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Βηματικός Κινητήρας 0.35kg.cm 5V</br>
    https://grobotronics.com/stepper-motor-0.35kg.cm.html
    </td>
    <td>3</td>
    <td>2,50€</td>
    <td>7,50 €</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Adafruit Αισθητήρας Απόστασης/Φωτός/RGB/Χειρονομίας - APDS9960<br/>
      https://grobotronics.com/adafruit-apds9960-proximity-light-rgb-and-gesture-sensor.html
  </td>
    <td>1</td>
    <td>9,50 €</td>
    <td>9,50 €</td>
  </tr>
  <tr>
    <td>8</td>
    <td>Γραμμικό Ρουλεμάν με Βάση - 10mm - SC10UU</br>
    https://grobotronics.com/linear-bearing-platform-small-10mm-diameter-sc10uu.html
    </td>
    <td>2</td>
    <td>4,80 €</td>
    <td>9,60 €</td>
  </tr>
  <tr>
    <td>9</td>
    <td>Horizontal Axis Bracket - SHF10<br/>
      https://grobotronics.com/horizontal-axis-bracket-shf10.html
  </td>
    <td>4</td>
    <td>3,90 €</td>
    <td>15,60 €</td>
  </tr>
  <tr>
    <td>10</td>
    <td>Jumper Wires 15cm Female to Male - Pack of 10<br/>
      https://grobotronics.com/break-away-headers-long.html
  </td>
    <td>1</td>
    <td>0,25 €</td>
    <td>0,25 €</td>
  </tr>
  <tr>
    <td>11</td>
    <td>Pin Header 1x40 Male Right Angle<br/>
      https://grobotronics.com/pin-header-1x40-male-right-angle.html
  </td>
    <td>1</td>
    <td>0,25 €</td>
    <td>0,25 €</td>
  </tr>
  <tr>
    <td>12</td>
    <td>Servo Micro 1.5kg.cm Continuous Rotation (Feetech FS90R)<br/>
      https://grobotronics.com/servo-micro-1.5kg.cm-continuous-rotation-feetech-fs90r.html
  </td>
    <td>2</td>
    <td>6,90 €</td>
    <td>13,80 €</td>
  </tr>
  <tr>
    <td colspan="4">Συνολική Τιμή</td>
    <td>187,20 €</td>
  </tr>
</table>

Θα χρησιμοποιηθούν επιπλέον υλικά από παλαιούς εκτυπωτές και CD-ROM.</br>
Για την κατασκευή θα χρησιμοποιηθεί επίσης ξύλο και χαρτόνι.

Μαθητές</br>
Μάρκος Χρήστος (ΕΠΑΛ Γ-Πληροφορικής)</br>
Ασλανίδης Κωνσταντίνος (ΕΠΑΛ Β-Πληροφορικής)</br>
Δόγκας Στέργιος (ΕΠΑΛ Β-Πληροφορικής)</br>
Κοντογιάννης Ιωάννης (ΕΠΑΛ Β-Πληροφορικής)</br>
Νίκου Νίκολαος (ΕΠΑΛ Β-Πληροφορικής)</br>
Νταρμπαϊσέλι Νούκρι (ΕΠΑΛ Β-Πληροφορικής)</br>
Ουζουνίδης Δημήτριος (ΕΠΑΛ Β-Πληροφορικής)</br>
Πηλιτσίδης Θεόδωρος (ΕΠΑΛ Β-Πληροφορικής)</br>
Τσάκουλι Αλέξανδρος (ΕΠΑΛ Β-Πληροφορικής)</br>
Χήρας Αθανάσιος (ΕΠΑΛ Β-Πληροφορικής)</br>


Εκπαιδευτικοί</br>
Δημητριάδης Γεώργιος (ΠΕ86 Πληροφορικής)</br>
Καράγαλης Αθανάσιος (ΠΕ86 Πληροφορικής)</br>
Μωϋσιάδης Βασίλειος (ΠΕ86 Πληροφορικής)</br>
