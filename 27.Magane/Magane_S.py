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

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
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
            RemoveUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.Table_Sin(cp, 22 + 45 * f.loop[cp], 100);
            f.Table_Cos(cp, 22 + 45 * f.loop[cp], 100);

            f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            RemoveUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.Table_Sin(cp, 22 + 45 * f.loop[cp], 50);
            f.Table_Cos(cp, 22 + 45 * f.loop[cp], 50);

            f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            RemoveUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 2, 50, 100, 100);
            f.NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 2, 50, -100, 100);
            f.NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 2, 50, 100, -100);
            f.NxNSquareShapeAt(cp, 1, "Kakaru (Twilight)", 2, 50, -100, -100);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, 100, 100);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, -100, 100);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, 100, -100);
            f.NxNSquareShapeAt(cp, 1, " Unit. Hoffnung 25000", 2, 50, -100, -100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         f.SkillEnd(cp);
      }
   }
}