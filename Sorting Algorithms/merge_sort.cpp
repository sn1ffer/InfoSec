#include "merge-sort.hpp"
#include <memory>

List::List(std::initializer_list<int> list) {
    ListElement * tail(nullptr);
    for (auto number : list){
        if (tail == nullptr) {
            head = std::make_unique<ListElement>(number);
            tail = head.get();
        } else {
            tail -> next = std::make_unique<ListElement>(number);
            tail = tail -> next.get();
        }
    }
}

auto merge(List a, List b) noexcept -> List {
    // Слияние двух упорядоченных списков
    List result;
    ListElement *tail = result.head.get();
    while (a.head && b.head) {
        // Выбираем меньший из a.head.value и b.head.value
        // и переносим a.head или b.head в конец result,
        // после чего переносим tail->next обратно
        // в a.head или b.head
        if (a.head->value < b.head->value) {
            if (result.head == nullptr) {
                result.head = std::move(a.head);
                tail = result.head.get();
                a.head = std::move(tail->next);
            } else {
                tail->next = std::move(a.head);
                tail = tail->next.get();
                a.head = std::move(tail->next);
            }
        } else {
            if (result.head == nullptr) {
                result.head = std::move(b.head);
                tail = result.head.get();
                b.head = std::move(tail->next);
            } else {
                tail->next = std::move(b.head);
                tail = tail->next.get();
                b.head = std::move(tail->next);
            }
        }
    }
        // переносим оставшийся список в конец result
    if (a.head != nullptr) {
        if (result.head == nullptr) {
            result.head = std::move(a.head);
        } else {
            tail->next = std::move(a.head);
        }
    }
    else if (b.head != nullptr){
        if (result.head == nullptr){
            result.head = std::move(b.head);
        }
        else {
            tail->next = std::move(b.head);
        }
    }
        return result;
}

auto mergesort(List &list) noexcept -> void {
    // Сортировка слиянием
    if (list.head == nullptr or list.head -> next == nullptr){
        return;
    }
    // 1. Определяем середину списка
    ListElement *middle = list.head.get();
    ListElement *f_middle = list.head.get();
    while (f_middle != nullptr and f_middle -> next != nullptr){
        f_middle = f_middle -> next -> next.get();
        if (middle -> next -> next != nullptr){
            middle = middle -> next.get();
        }
    }
    // 2. Переносим вторую половину в новый список
    List second;
    second.head = std::move(middle -> next);
    // 3. Для каждой половины запускаем mergesort
    mergesort(list);
    mergesort(second);
    // 4. Делаем merge от результатов,
    // не забыв std::move в аргументах,
    // присваивая результат в list
    list = merge(std::move(list), std::move(second));
}
