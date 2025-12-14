#include <stdio.h>
#include <wchar.h>
#include <string.h>
#include <locale.h>
#include <stdlib.h>

wchar_t* CharToWChar(const char* multiByte);

int main(int argc, char* argv[])
{
    setlocale(LC_ALL, "");

    // 매개변수 검사 (입력 단어가 있는가? 단어 파일의 경로가 있는가?)
    if (argc < 3)
    {
        wprintf(L"잘못된 매개변수 입력.\n");
        wprintf(L"올바른 매개변수 : worch.exe \"입력 단어\" \"단어 파일의 경로\"\n");

        return 1;
    }

    wchar_t* word = CharToWChar(argv[1]);

    wprintf(L"입력한 단어 : %ls\n", word);

    FILE* fp = fopen(argv[2], "w, ccs=UTF-8");

    if (fp == NULL)
    {
        wprintf(L"단어 파일 열기 실패.\n");

        if (word != NULL)
        {
            free(word);
        }

        return 1;
    }

    fwprintf(fp, word);
    fclose(fp);

    if (word != NULL)
    {
        free(word);
    }

    return 0;
}

wchar_t* CharToWChar(const char* multiByte)
{
    size_t size = strlen(multiByte) + 1;
    wchar_t* wide = (wchar_t*)malloc(size);
    size_t converted = mbstowcs(wide, multiByte, size);

    if (converted == (size_t) - 1)
    {
        free(wide);

        return NULL;
    }

    return wide;
}