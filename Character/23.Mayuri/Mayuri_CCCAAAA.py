import Function as f;

const s = StringBuffer();

function main(cp)
{
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 8)
         {       
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");

            if (f.loop[cp] % 2 == 0)
            {
               KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
               KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

               f.Table_Sin(cp, (45 * f.loop[cp] + 22), 100);
               f.Table_Cos(cp, (45 * f.loop[cp] + 22), 100); 

               f.DotShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
               f.DotShape(cp, 1, "40 + 1n Wraith", -f.CosAngle[cp], -f.SinAngle[cp]);
               f.DotShape(cp, 1, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);
               f.DotShape(cp, 1, "40 + 1n Zealot", -f.CosAngle[cp], -f.SinAngle[cp]);
               f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp]);
               f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp]);
               f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp]);
               f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp]);

               f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 7, 150);
               KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

               f.Table_Sin(cp, (22 * f.loop[cp] + 22), 50 * (f.loop[cp] / 2) + 50);
               f.Table_Cos(cp, (22 * f.loop[cp] + 22), 50 * (f.loop[cp] / 2) + 50); 

               f.SquareShape(cp, 1, "60 + 1n Siege", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp]);

               KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
               KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
               KillUnitAt(All, "Target", "Anywhere", cp);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
               Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            }
            else
            {
               KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
               KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

               f.Table_Sin(cp, (45 * f.loop[cp] + 112), 100);
               f.Table_Cos(cp, (45 * f.loop[cp] + 112), 100); 

               f.DotShape(cp, 1, "40 + 1n Mojo", f.CosAngle[cp], f.SinAngle[cp]);
               f.DotShape(cp, 1, "40 + 1n Mojo", -f.CosAngle[cp], -f.SinAngle[cp]);
               f.DotShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
               f.DotShape(cp, 1, "Protoss Dark Archon", -f.CosAngle[cp], -f.SinAngle[cp]);
               f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp]);
               f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp]);
               f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp]);
               f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp]);

               f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 7, 150);
               KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

               KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
               KillUnitAt(All, "Target", "Anywhere", cp);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
               Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
            }

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 16)
         {       
            if (f.loop[cp] % 2 == 0)
            {
               KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
               KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

               f.Table_Sin(cp, (45 * f.loop[cp] + 22), 100);
               f.Table_Cos(cp, (45 * f.loop[cp] + 22), 100); 

               f.DotShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
               f.DotShape(cp, 1, "40 + 1n Wraith", -f.CosAngle[cp], -f.SinAngle[cp]);
               f.DotShape(cp, 1, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);
               f.DotShape(cp, 1, "40 + 1n Zealot", -f.CosAngle[cp], -f.SinAngle[cp]);
               f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp]);
               f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp]);
               f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp]);
               f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp]);

               f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 7, 150);
               KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

               f.Table_Sin(cp, (22 * f.loop[cp] + 112), 50 * (f.loop[cp] / 2 - 4) + 50);
               f.Table_Cos(cp, (22 * f.loop[cp] + 112), 50 * (f.loop[cp] / 2 - 4) + 50); 

               f.SquareShape(cp, 1, "60 + 1n Siege", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp]);

               KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
               KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
               KillUnitAt(All, "Target", "Anywhere", cp);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
               Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
            }
            else
            {
               KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
               KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

               f.Table_Sin(cp, (45 * f.loop[cp] + 112), 100);
               f.Table_Cos(cp, (45 * f.loop[cp] + 112), 100); 

               f.DotShape(cp, 1, "40 + 1n Mojo", f.CosAngle[cp], f.SinAngle[cp]);
               f.DotShape(cp, 1, "40 + 1n Mojo", -f.CosAngle[cp], -f.SinAngle[cp]);
               f.DotShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
               f.DotShape(cp, 1, "Protoss Dark Archon", -f.CosAngle[cp], -f.SinAngle[cp]);
               f.DotShape(cp, 1, "Target", -f.SinAngle[cp], f.CosAngle[cp]);
               f.DotShape(cp, 1, "Target", f.SinAngle[cp], -f.CosAngle[cp]);
               f.DotShape(cp, 1, " Creep. Dunkelheit", -f.SinAngle[cp], f.CosAngle[cp]);
               f.DotShape(cp, 1, " Creep. Dunkelheit", f.SinAngle[cp], -f.CosAngle[cp]);

               f.EdgeShape(cp, 1, "60 + 1n High Templar", 45, 7, 150);
               KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

               KillUnitAt(All, "Target", "Anywhere", cp);
               KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
               Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
               Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
            }

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 16)
         {       
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            f.Voice_Routine(cp, 9);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {        
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 5, 150);
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 150);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 960);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 5)
         {
            if (f.loop[cp] % 2 == 1)
            {
               f.EdgeShape(cp, 1, " Creep. Dunkelheit", 0, 4, 100);
               f.EdgeShape(cp, 1, " Creep. Dunkelheit", 0, 2, 50);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
            }
            else
            {
               KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
            }

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 5, 150);
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 150);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 480);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         f.SkillEnd(cp);
      }
   }
}