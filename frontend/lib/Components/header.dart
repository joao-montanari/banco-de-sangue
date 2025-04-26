import 'package:flutter/material.dart';
import 'package:frontend/Components/button.dart';

class CustomHeader extends StatefulWidget implements PreferredSizeWidget {
  const CustomHeader({
    super.key,
    this.title,
  });

  final String? title;

  @override
  State<CustomHeader> createState() => _CustomHeader();

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}

class _CustomHeader extends State<CustomHeader> {

  void redirect() {
    print('redirect function');
  }

  @override
  Widget build(BuildContext context) {
    return AppBar(
      backgroundColor: Color(0xffDF222B),
      actions: [
        Expanded(
          child: Row(
            mainAxisSize: MainAxisSize.max,
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Padding(
                padding: const EdgeInsets.only(left: 120),
                child: Text(
                  widget.title ?? '',
                  style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.w600,
                    color: Color(0xffFFFFFF),
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(right: 120),
                child: Row(
                  spacing: 10.0,
                  children: [
                    CustomButton(
                      label: 'Porque Doar', 
                      onPressed: redirect,
                      design: 'secundary',
                    ),
                    CustomButton(
                      label: 'Requisitos para Doar', 
                      onPressed: redirect,
                      design: 'secundary',
                    ),
                    CustomButton(
                      label: 'Entrar como médico', 
                      onPressed: redirect,
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}