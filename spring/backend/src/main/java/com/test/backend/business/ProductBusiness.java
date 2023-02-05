package com.test.backend.business;

import com.test.backend.exception.BaseException;
import com.test.backend.exception.ProductException;
import org.springframework.stereotype.Service;

import java.util.Objects;

@Service
public class ProductBusiness {

    public String getProductById(String id) throws BaseException {
        // TODO: Get data from database
        if (!Objects.equals("1234", id)){
            throw ProductException.notFound();
        }
        return id;
    }
}
