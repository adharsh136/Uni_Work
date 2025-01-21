CREATE VIEW CustomerSummary AS
SELECT customerId,
    modelName,
    SUM((julianday(dateBack)-julianday(dateOut)) + 1) as daysRented,
    IIF(substr(dateBack,6,2)>'06',
        substr(dateBack,1,4) || '/' || (IIF(substr(dateBack,3,2)<9, '0' || substr(dateBack,3,2)+1, substr(dateBack,3,2) + 1)),
        (substr(dateBack,1,4)-1) || '/' || substr(dateBack,3,2)
        ) as taxYear,
    SUM(rentalCost) as rentalCost FROM rentalContract LEFT JOIN Phone USING (IMEI) WHERE dateBack IS NOT NULL GROUP BY customerId,taxYear,modelName;