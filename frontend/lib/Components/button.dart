import 'package:flutter/material.dart';

class CustomButton extends StatefulWidget {
  const CustomButton({
    super.key,
    required this.label,
    required this.onPressed,
    this.design = 'primary',
    this.icon,
  });

  final String label;
  final Function onPressed;
  final String? design;
  final Icons? icon;

  @override
  State<CustomButton> createState() => _CustomButton();
}

class _CustomButton extends State<CustomButton> {
  @override
  Widget build(BuildContext context) {
    return ElevatedButton.icon(
      onPressed: () => widget.onPressed, 
      label: Text(
        widget.label,
        style: TextStyle(
          color: Color(
            widget.design == 'secundary' ? 0xffFFFFFF : 0xff000000,
          ),
          fontSize: 15,
        ),
      ),
      style: ElevatedButton.styleFrom(
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(4.0),
        ),
        backgroundColor: Color(
          widget.design == 'secundary' ? 0xffDF222B : 0xffFFFFFF,
        ),
        elevation: widget.design == 'secundary' ? 0 : 1.5,
        minimumSize: Size(
          80, 
          widget.design == 'secundary' ? 80 : 40,
        ),

        overlayColor: Color(0xffFFFFFF),

      ),
    );
  }
}