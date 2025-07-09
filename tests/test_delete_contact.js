const { Builder, By, until } = require('selenium-webdriver');

async function testDeleteContact() {
  let driver = await new Builder().forBrowser('chrome').build();

  try {
    await driver.get('http://localhost:3000');

    // Esperamos a que cargue la tabla y busque el primer botón "Delete"
    await driver.wait(until.elementLocated(By.css('.btn-danger')), 5000);

    // Hacemos clic en el primer botón "Delete"
    const deleteButton = await driver.findElement(By.css('.btn-danger'));
    await deleteButton.click();

    // Esperar un momento para que se actualice la tabla
    await driver.sleep(3000);

    console.log('✅ Contacto eliminado exitosamente (se hizo clic en el botón Delete)');
  } catch (error) {
    console.error('❌ Hubo un error al intentar eliminar el contacto:', error);
  } finally {
    await driver.quit();
  }
}

testDeleteContact();
