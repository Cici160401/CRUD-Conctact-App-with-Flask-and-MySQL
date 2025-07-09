const { Builder, By, until } = require('selenium-webdriver');

(async function testAddContact() {
  let driver = await new Builder().forBrowser('chrome').build();

  try {
    // 1. Abrimos la app local
    await driver.get('http://127.0.0.1:3000');

    // 2. Llenamos los campos del formulario
    await driver.findElement(By.name('fullname')).sendKeys('Juan Pérez');
    await driver.findElement(By.name('phone')).sendKeys('123456789');
    await driver.findElement(By.name('email')).sendKeys('juanperez@example.com');

    // 3. Presionamos el botón "Save"
    await driver.findElement(By.css('button[type="submit"]')).click();

    // 4. Esperamos que se recargue la tabla con el nuevo contacto
    await driver.wait(until.elementLocated(By.xpath("//td[contains(text(),'Juan Pérez')]")), 5000);

    console.log('✅ Contacto agregado exitosamente');
    console.log(`URL actual después de presionar Save vacío: ${url}`);

  } catch (err) {
    console.error('❌ Error en la prueba:', err.message);
  } finally {
    await driver.quit(); // Cerramos el navegador
  }
})();
