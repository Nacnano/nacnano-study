package com.test.backend.api;

import com.test.backend.business.TestBusiness;
import com.test.backend.exception.UserException;
import com.test.backend.model.MRegisterRequest;
import com.test.backend.model.TestResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/test")
public class TestApi {

    //Method 1
//    @Autowired
//    private TestBusiness business;

    //Method 2
    private final TestBusiness business;

    public TestApi(TestBusiness business) {
        this.business = business;
    }

    @GetMapping
    public TestResponse test() {
        TestResponse  response = new TestResponse();
        response.setName("Nac");
        response.setFood("Pizza");

        return response;
    }


    @PostMapping
    @RequestMapping("/register")
    public ResponseEntity<String> register(@RequestBody MRegisterRequest request) throws UserException {
        String response = business.register(request);
        return ResponseEntity.ok(response);
    }
    public static void main(String[] args){
    }
}
