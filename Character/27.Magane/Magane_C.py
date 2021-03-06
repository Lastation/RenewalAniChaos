import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 4)
         {             
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Mutalisk", 0, 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, "Anywhere");

            f.Table_Sin(cp, 90 * f.loop[cp], 150);
            f.Table_Cos(cp, 90 * f.loop[cp], 150);

            f.DotShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 8)
         {             
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.DotShape(cp, 1, "40 + 1n Mutalisk", 0, 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, "Anywhere");

            f.Table_Sin(cp, 90 * f.loop[cp] + 45, 150);
            f.Table_Cos(cp, 90 * f.loop[cp] + 45, 150);

            f.DotShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            RemoveUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 2)
         {       
            f.Table_Sin(cp, 90 * f.loop[cp] + 45, f.loop[cp] * 75 + 75);
            f.Table_Cos(cp, 90 * f.loop[cp] + 45, f.loop[cp] * 75 + 75);

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.Table_Sin(cp, 90 * f.loop[cp], f.loop[cp] * 75 + 75);
            f.Table_Cos(cp, 90 * f.loop[cp], f.loop[cp] * 75 + 75);

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            f.Table_Sin(cp, 90 * f.loop[cp] + 45, 150);
            f.Table_Cos(cp, 90 * f.loop[cp] + 45, 150);

            f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 90 * f.loop[cp], 150);
            f.Table_Cos(cp, 90 * f.loop[cp], 150);

            f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.Table_Sin(cp, 90 * f.loop[cp] + 45, 75);
            f.Table_Cos(cp, 90 * f.loop[cp] + 45, 75);

            f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 90 * f.loop[cp], 75);
            f.Table_Cos(cp, 90 * f.loop[cp], 75);

            f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);


         f.SkillEnd(cp);
      }
   }
}