package com.example.drintelligent;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class MainActivity5 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main5);
        Button btn = findViewById(R.id.select_file);
        btn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                openfilechooser(view);
            }
        });
        Button btn1 = findViewById(R.id.upload);
        btn1.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                newWindow();
            }
        });
    }



    int requestcode = 1;


    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        Context context = getApplicationContext();
        if(requestCode == requestCode && resultCode == Activity.RESULT_OK){
            if(data == null){
                return;
            }
            Uri uri = data.getData();
            Toast.makeText(context, uri.getPath(), Toast.LENGTH_SHORT).show();
        }
    }
    public void openfilechooser(View view){
        Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
        intent.setType("application/pdf");
        startActivityForResult(intent, 86);
    }
    private void newWindow() {
        Toast.makeText(this, "Uploading", Toast.LENGTH_SHORT).show();
        Intent intent  = new Intent(getApplicationContext(), MainActivity6.class);
        startActivity(intent);
    }

}
