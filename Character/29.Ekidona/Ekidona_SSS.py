import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.Table_Sin(cp, 22, 150);
            f.Table_Cos(cp, 22, 150);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "40 + 1n Gantrithor", x, y);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }
         else if (f.loop[cp] == 2)
         {
            f.Table_Sin(cp, 67, 150);
            f.Table_Cos(cp, 67, 150);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.Table_Sin(cp, 22, 100);
            f.Table_Cos(cp, 22, 100);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "60 + 1n Danimoth", x, y);
            f.SquareShape(cp, 1, "60 + 1n Archon", x, y);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 4)
         {
            f.Table_Sin(cp, 67, 200);
            f.Table_Cos(cp, 67, 200);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "40 + 1n Gantrithor", x, y);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }
         else if (f.loop[cp] == 6)
         {
            f.Table_Sin(cp, 22, 200);
            f.Table_Cos(cp, 22, 200);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.Table_Sin(cp, 67, 150);
            f.Table_Cos(cp, 67, 150);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "60 + 1n Danimoth", x, y);
            f.SquareShape(cp, 1, "60 + 1n Archon", x, y);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            f.Table_Sin(cp, 67, 100);
            f.Table_Cos(cp, 67, 100);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "60 + 1n High Templar", x, y);
            f.SquareShape(cp, 8, " Unit. Schnee", x, y);
            KillUnitAt(All, " Unit. Schnee", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 4)
         {
            f.Table_Sin(cp, 22, 150);
            f.Table_Cos(cp, 22, 150);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "60 + 1n High Templar", x, y);
            f.SquareShape(cp, 8, " Unit. Schnee", x, y);
            KillUnitAt(All, " Unit. Schnee", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 20)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
         f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}