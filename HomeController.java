package com.indoinves.home;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import java.time.Year;

@Controller
public class HomeController {

    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("currentYear", Year.now().getValue());
        return "index"; // Memuat file index.html di folder templates
    }
}
