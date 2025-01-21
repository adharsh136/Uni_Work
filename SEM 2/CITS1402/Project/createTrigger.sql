CREATE TRIGGER cost_calculation
    AFTER UPDATE ON rentalContract
    WHEN old.dateBack IS NULL AND new.dateBack IS NOT NULL
BEGIN
    UPDATE rentalContract 
        SET rentalCost = round((SELECT baseCost+(dailyCost*(julianday(new.dateBack)-julianday(new.dateOut)+1)) from
            PhoneModel join Phone using (modelNumber,modelName)
            WHERE Phone.IMEI=new.IMEI),2)
        WHERE customerId = new.customerId and IMEI = new.IMEI;
END;