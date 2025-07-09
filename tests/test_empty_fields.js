const { Builder, By, until } = require('selenium-webdriver');

(async function testEmptyFields() {
    const driver = await new Builder().forBrowser('chrome').build();

    try {
        await driver.get('http://127.0.0.1:3000');

        // Esperar que cargue el botón Save
        await driver.wait(until.elementLocated(By.css('button[type="submit"]')), 5000);

        // Click en botón Save sin rellenar nada
        const saveButton = await driver.findElement(By.css('button[type="submit"]'));
        await saveButton.click();

        // Esperar un momento por si aparece alerta o no pasa nada
        await driver.sleep(1000);

        // Verificar si se quedó en la misma página (opcional)
        const url = await driver.getCurrentUrl();
        console.log(`URL actual después de presionar Save vacío: ${url}`);
     // Verificar si se muestra un mensaje de alerta (esto depende de que uses flash en tu app Flask)
        try {
        const alert = await driver.findElement(By.className('alert'));
        const message = await alert.getText();

        if (message.includes("obligatorios")) {
            console.log("✅ Test aprobado: La app evitó guardar contacto vacío y mostró mensaje.");
        } else {
            console.log("⚠️ Test con comportamiento inesperado: Se mostró otra alerta.");
        }
        } catch (error) {
        console.log("❌ Test fallido: Se pudo guardar un contacto vacío o no hubo validación.");
        }

    } finally {        
        await driver.quit();
    }
})();
