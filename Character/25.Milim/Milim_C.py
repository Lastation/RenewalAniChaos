import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 4)
         {      
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.Table_Sin(cp, 45 * f.loop[cp], 50);
            f.Table_Cos(cp, 45 * f.loop[cp], 50);

            f.DotShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
            f.DotShape(cp, 1, "40 + 1n Wraith", -f.CosAngle[cp], -f.SinAngle[cp]);
            f.DotShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
            f.DotShape(cp, 1, "Protoss Dark Archon", -f.CosAngle[cp], -f.SinAngle[cp]);

            f.Table_Sin(cp, 45 * f.loop[cp] + 45, 50);
            f.Table_Cos(cp, 45 * f.loop[cp] + 45, 50);

            f.DotShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);
            f.DotShape(cp, 1, "Kakaru (Twilight)", -f.CosAngle[cp], -f.SinAngle[cp]);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "Target", 50, 0);
            f.SquareShape(cp, 1, "Target", 100, 0);
            KillUnitAt(All, "Target", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            f.SquareShape(cp, 1, "Target", 50, 50);
            f.SquareShape(cp, 1, "Target", 100, 100);
            KillUnitAt(All, "Target", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {         
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 50, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 50);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 0);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {         
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 50, 100);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 50);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Goliath", 50, 100);
            f.SquareShape(cp, 1, "40 + 1n Goliath", 100, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {         
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Guardian", 50, 100);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 50);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 50, 100);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 100, 50);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 9)
         {         
            f.SquareShape(cp, 1, "40 + 1n Guardian", 100, 150);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 150, 100);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 100, 150);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 150, 100);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 10)
         {         
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 50, 100);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 50);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 150);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", 150, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 11)
         {       
            f.SquareShape(cp, 1, "80 + 1n Tom Kazansky", 100, 150);
            f.SquareShape(cp, 1, "80 + 1n Tom Kazansky", 150, 100);
            KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 100);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 100, 50);

            f.SquareShape(cp, 1, "Protoss Dark Archon", 50, 100);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 100, 50);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 100, 150);
            f.SquareShape(cp, 1, "Protoss Dark Archon", 150, 100);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         f.SkillEnd(cp);
      }
   }
}